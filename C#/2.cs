using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LeetCode
{
    internal class Program
    {
        static void Main(string[] args)
        {
        }


        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            if (l1.next == null && l2.next == null)
            {
                if (l1.val + l2.val >= 10)
                {
                    int carry = (l1.val + l2.val) / 10;
                    return new ListNode((l1.val + l2.val) % 10, new ListNode(carry, null));
                }
                else
                    return new ListNode(l1.val + l2.val);
            }
            else if(l1.next == null)
            {
                if (l1.val + l2.val >= 10)
                {
                    int carry = (l1.val + l2.val) / 10;
                    return new ListNode((l1.val + l2.val) % 10, AddTwoNumbers(new ListNode(carry, null), l2.next));
                }
                else
                    return new ListNode(l1.val + l2.val, AddTwoNumbers( new ListNode(0,null), l2.next));
            }
            else if(l2.next == null)
            {
                if(l1.val + l2.val >= 10)
                {
                    int carry = (l1.val + l2.val) / 10;
                    return new ListNode((l1.val + l2.val) % 10, AddTwoNumbers(new ListNode(carry, null), l1.next));
                }
                else
                    return new ListNode(l1.val + l2.val, AddTwoNumbers(l1.next,new ListNode(0,null)));
            }
            else
            {
                if(l1.val + l2.val >= 10)
                {
                    int carry = (l1.val + l2.val) / 10;
                    return new ListNode((l1.val + l2.val) % 10, AddTwoNumbers(new ListNode(carry, null), AddTwoNumbers(l1.next, l2.next)));
                }
                else
                    return new ListNode(l1.val + l2.val, AddTwoNumbers(l1.next, l2.next));
            }


        }
    }


   public class ListNode
   {
      public int val;
      public ListNode next;
     public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
       }
  }




}
